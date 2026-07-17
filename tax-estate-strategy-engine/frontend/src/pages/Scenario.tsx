import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getScenario } from "../api/scenario";
import { getReport } from "../api/strategies";
import type { ScenarioSummary } from "../types/Scenario";
import StrategyList from "../components/StrategyList";

type ScenarioState =
  | { status: "loading" }
  | { status: "error"; message: string }
  | { status: "success"; scenario: ScenarioSummary };

export default function Scenario() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [state, setState] = useState<ScenarioState>({ status: "loading" });
  const [isDownloading, setIsDownloading] = useState(false);

  useEffect(() => {
    if (!id) return;
    let cancelled = false;
    setState({ status: "loading" });

    getScenario(id)
      .then((scenario) => {
        if (!cancelled) setState({ status: "success", scenario });
      })
      .catch((error: unknown) => {
        if (!cancelled) {
          setState({
            status: "error",
            message: error instanceof Error ? error.message : "Failed to load scenario.",
          });
        }
      });

    return () => {
      cancelled = true;
    };
  }, [id]);

  async function handleDownload() {
    if (!id) return;
    setIsDownloading(true);
    try {
      const report = await getReport(id);
      const blob = new Blob([report.markdown], { type: "text/markdown" });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = `${id}-strategy-report.md`;
      link.click();
      URL.revokeObjectURL(url);
    } finally {
      setIsDownloading(false);
    }
  }

  if (!id) {
    return <p className="p-6 text-sm text-red-600">No scenario id provided.</p>;
  }

  if (state.status === "loading") {
    return <p className="p-6 text-sm text-slate-500">Loading scenario…</p>;
  }

  if (state.status === "error") {
    return <p className="p-6 text-sm text-red-600">{state.message}</p>;
  }

  const { scenario } = state;

  return (
    <div className="mx-auto max-w-5xl px-6 py-12">
      <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <h1 className="text-2xl font-bold text-slate-900">Scenario {scenario.id}</h1>
        <dl className="mt-4 grid grid-cols-2 gap-4 sm:grid-cols-4">
          <div>
            <dt className="text-xs font-medium uppercase tracking-wide text-slate-400">Tax year</dt>
            <dd className="mt-1 text-sm font-semibold text-slate-900">{scenario.tax_year ?? "—"}</dd>
          </div>
          <div>
            <dt className="text-xs font-medium uppercase tracking-wide text-slate-400">Filing status</dt>
            <dd className="mt-1 text-sm font-semibold text-slate-900">{scenario.filing_status ?? "—"}</dd>
          </div>
          <div>
            <dt className="text-xs font-medium uppercase tracking-wide text-slate-400">Income range</dt>
            <dd className="mt-1 text-sm font-semibold text-slate-900">{scenario.income_range ?? "—"}</dd>
          </div>
          <div>
            <dt className="text-xs font-medium uppercase tracking-wide text-slate-400">State</dt>
            <dd className="mt-1 text-sm font-semibold text-slate-900">{scenario.state ?? "—"}</dd>
          </div>
        </dl>

        <div className="mt-6 flex gap-3">
          <button
            type="button"
            onClick={() => navigate(`/scenario/${scenario.id}/report`)}
            className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white shadow-sm transition hover:bg-slate-700"
          >
            View Report
          </button>
          <button
            type="button"
            onClick={handleDownload}
            disabled={isDownloading}
            className="rounded-md border border-slate-300 bg-white px-4 py-2 text-sm font-medium text-slate-700 shadow-sm transition hover:bg-slate-50 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {isDownloading ? "Preparing…" : "Download Report"}
          </button>
        </div>
      </div>

      <div className="mt-8">
        <h2 className="mb-4 text-lg font-semibold text-slate-900">Ranked Strategies</h2>
        <StrategyList scenarioId={scenario.id} />
      </div>
    </div>
  );
}
