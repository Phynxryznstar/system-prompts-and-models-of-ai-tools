import { useEffect, useState } from "react";
import { getRanking, getReasoning, getScoring } from "../api/strategies";
import type { StrategyResult } from "../types/Strategy";
import StrategyCard from "./StrategyCard";

interface StrategyListProps {
  scenarioId: string;
}

type StrategyListState =
  | { status: "loading" }
  | { status: "error"; message: string }
  | { status: "success"; reasoningCount: number; scoringCount: number; ranked: StrategyResult[] };

export default function StrategyList({ scenarioId }: StrategyListProps) {
  const [state, setState] = useState<StrategyListState>({ status: "loading" });

  useEffect(() => {
    let cancelled = false;
    setState({ status: "loading" });

    Promise.all([getReasoning(scenarioId), getScoring(scenarioId), getRanking(scenarioId)])
      .then(([reasoning, scoring, ranking]) => {
        if (cancelled) return;
        setState({
          status: "success",
          reasoningCount: reasoning.length,
          scoringCount: scoring.length,
          ranked: ranking.strategies,
        });
      })
      .catch((error: unknown) => {
        if (cancelled) return;
        setState({
          status: "error",
          message: error instanceof Error ? error.message : "Failed to load strategies.",
        });
      });

    return () => {
      cancelled = true;
    };
  }, [scenarioId]);

  if (state.status === "loading") {
    return <p className="text-sm text-slate-500">Loading strategies…</p>;
  }

  if (state.status === "error") {
    return <p className="text-sm text-red-600">{state.message}</p>;
  }

  if (state.ranked.length === 0) {
    return <p className="text-sm text-slate-500">No strategies were identified for this scenario.</p>;
  }

  return (
    <div>
      <p className="mb-4 text-sm text-slate-500">
        {state.reasoningCount} strategies identified, {state.scoringCount} scored, ranked by weighted benefit below.
      </p>
      <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
        {state.ranked.map((strategy) => (
          <StrategyCard key={strategy.name} strategy={strategy} />
        ))}
      </div>
    </div>
  );
}
