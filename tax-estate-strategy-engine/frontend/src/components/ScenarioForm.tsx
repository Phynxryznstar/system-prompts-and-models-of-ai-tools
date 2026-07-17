import { useState } from "react";
import type { ChangeEvent, FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import { ingestScenario } from "../api/scenario";
import type { ClientScenarioPayload } from "../types/Scenario";

export default function ScenarioForm() {
  const navigate = useNavigate();
  const [jsonText, setJsonText] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  function handleFileChange(event: ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = () => {
      setJsonText(typeof reader.result === "string" ? reader.result : "");
    };
    reader.readAsText(file);
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);

    let payload: ClientScenarioPayload;
    try {
      payload = JSON.parse(jsonText) as ClientScenarioPayload;
    } catch {
      setError("That doesn't look like valid JSON. Check the formatting and try again.");
      return;
    }

    setIsSubmitting(true);
    try {
      const result = await ingestScenario(payload);
      navigate(`/scenario/${result.scenario_id}`);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to ingest scenario.");
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="scenario-file" className="block text-sm font-medium text-slate-700">
          Upload a scenario JSON file
        </label>
        <input
          id="scenario-file"
          type="file"
          accept="application/json"
          onChange={handleFileChange}
          className="mt-1 block w-full text-sm text-slate-600 file:mr-4 file:rounded-md file:border-0 file:bg-slate-900 file:px-4 file:py-2 file:text-sm file:font-medium file:text-white hover:file:bg-slate-700"
        />
      </div>

      <div>
        <label htmlFor="scenario-json" className="block text-sm font-medium text-slate-700">
          Or paste scenario JSON
        </label>
        <textarea
          id="scenario-json"
          value={jsonText}
          onChange={(event) => setJsonText(event.target.value)}
          rows={14}
          placeholder='{"id": "scenario_001", "tax_year": 2026, ...}'
          className="mt-1 block w-full rounded-md border border-slate-300 bg-white p-3 font-mono text-sm text-slate-900 shadow-sm focus:border-slate-500 focus:outline-none focus:ring-1 focus:ring-slate-500"
        />
      </div>

      {error && <p className="text-sm text-red-600">{error}</p>}

      <button
        type="submit"
        disabled={isSubmitting || jsonText.trim().length === 0}
        className="rounded-md bg-slate-900 px-4 py-2 text-sm font-medium text-white shadow-sm transition hover:bg-slate-700 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {isSubmitting ? "Ingesting…" : "Ingest scenario"}
      </button>
    </form>
  );
}
