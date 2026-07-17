import { useState } from "react";
import ScenarioForm from "../components/ScenarioForm";

export default function Home() {
  const [showForm, setShowForm] = useState(false);

  return (
    <div className="mx-auto max-w-3xl px-6 py-16">
      <div className="text-center">
        <h1 className="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
          Tax + Estate Strategy Engine
        </h1>
        <p className="mt-4 text-lg text-slate-600">
          Ingest a client scenario, then let the reasoning, scoring, and ranking engines surface
          and prioritize applicable tax, estate, and state strategies.
        </p>
        <button
          type="button"
          onClick={() => setShowForm((value) => !value)}
          className="mt-8 rounded-md bg-slate-900 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition hover:bg-slate-700"
        >
          {showForm ? "Hide form" : "Create / ingest a scenario"}
        </button>
      </div>

      {showForm && (
        <div className="mt-10 rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
          <ScenarioForm />
        </div>
      )}
    </div>
  );
}
