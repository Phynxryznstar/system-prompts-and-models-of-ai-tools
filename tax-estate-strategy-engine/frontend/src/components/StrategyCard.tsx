import type { StrategyResult } from "../types/Strategy";

interface StrategyCardProps {
  strategy: StrategyResult;
}

const TYPE_BADGE_STYLES: Record<string, string> = {
  tax: "bg-blue-100 text-blue-800",
  estate: "bg-purple-100 text-purple-800",
  state: "bg-amber-100 text-amber-800",
  combined: "bg-emerald-100 text-emerald-800",
};

function formatCurrency(value: number | null): string {
  if (value === null) return "—";
  return value.toLocaleString("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0,
  });
}

function buildSummary(strategy: StrategyResult): string {
  const parts: string[] = [];

  if (strategy.related_entities.length > 0) {
    parts.push(`${strategy.related_entities.length} ${strategy.related_entities.length === 1 ? "entity" : "entities"}`);
  }
  if (strategy.related_activities.length > 0) {
    parts.push(
      `${strategy.related_activities.length} ${strategy.related_activities.length === 1 ? "activity" : "activities"}`,
    );
  }
  if (strategy.related_assets.length > 0) {
    parts.push(`${strategy.related_assets.length} ${strategy.related_assets.length === 1 ? "asset" : "assets"}`);
  }
  if (strategy.related_sections.length > 0) {
    parts.push(`IRC ${strategy.related_sections.join(", ")}`);
  }
  if (strategy.related_constraints.length > 0) {
    parts.push(`triggered by ${strategy.related_constraints.join(", ")}`);
  }

  return parts.length > 0 ? parts.join(" · ") : "No related graph context captured.";
}

export default function StrategyCard({ strategy }: StrategyCardProps) {
  const badgeClass = TYPE_BADGE_STYLES[strategy.type] ?? "bg-slate-100 text-slate-800";

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition hover:shadow-md">
      <div className="flex items-start justify-between gap-4">
        <h3 className="text-base font-semibold text-slate-900">{strategy.name}</h3>
        <span className={`shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium capitalize ${badgeClass}`}>
          {strategy.type}
        </span>
      </div>

      <p className="mt-2 text-sm text-slate-600">{buildSummary(strategy)}</p>

      <dl className="mt-4 grid grid-cols-2 gap-4 border-t border-slate-100 pt-4">
        <div>
          <dt className="text-xs font-medium uppercase tracking-wide text-slate-400">Raw score</dt>
          <dd className="mt-1 text-lg font-semibold text-slate-900">{formatCurrency(strategy.raw_score)}</dd>
        </div>
        <div>
          <dt className="text-xs font-medium uppercase tracking-wide text-slate-400">Weighted score</dt>
          <dd className="mt-1 text-lg font-semibold text-slate-900">{formatCurrency(strategy.weighted_score)}</dd>
        </div>
      </dl>
    </div>
  );
}
