import { apiClient } from "./client";
import type { RankingResponse, StrategyResult } from "../types/Strategy";
import type { ReportResponse } from "../types/Report";

/** GET /strategies/{scenario_id}/reasoning */
export async function getReasoning(scenarioId: string): Promise<StrategyResult[]> {
  const { data } = await apiClient.get<StrategyResult[]>(`/strategies/${scenarioId}/reasoning`);
  return data;
}

/** GET /strategies/{scenario_id}/scoring */
export async function getScoring(scenarioId: string): Promise<StrategyResult[]> {
  const { data } = await apiClient.get<StrategyResult[]>(`/strategies/${scenarioId}/scoring`);
  return data;
}

/** GET /strategies/{scenario_id}/ranking */
export async function getRanking(scenarioId: string): Promise<RankingResponse> {
  const { data } = await apiClient.get<RankingResponse>(`/strategies/${scenarioId}/ranking`);
  return data;
}

/** GET /strategies/{scenario_id}/report */
export async function getReport(scenarioId: string): Promise<ReportResponse> {
  const { data } = await apiClient.get<ReportResponse>(`/strategies/${scenarioId}/report`);
  return data;
}
