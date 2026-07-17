import { apiClient } from "./client";
import type { ClientScenarioPayload, IngestionResult, ScenarioSummary } from "../types/Scenario";

/** GET /scenario/{scenario_id} */
export async function getScenario(scenarioId: string): Promise<ScenarioSummary> {
  const { data } = await apiClient.get<ScenarioSummary>(`/scenario/${scenarioId}`);
  return data;
}

/** POST /scenario/ingest */
export async function ingestScenario(payload: ClientScenarioPayload): Promise<IngestionResult> {
  const { data } = await apiClient.post<IngestionResult>("/scenario/ingest", payload);
  return data;
}
