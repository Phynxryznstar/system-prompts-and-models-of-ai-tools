// Mirrors api/models.py: StrategyResult and RankingResponse.

export type StrategyType = "tax" | "estate" | "state" | "combined";

export interface StrategyResult {
  name: string;
  type: StrategyType;
  related_entities: string[];
  related_activities: string[];
  related_assets: string[];
  related_constraints: string[];
  related_sections: string[];
  estimated_inputs: Record<string, unknown>;
  raw_score: number | null;
  weighted_score: number | null;
}

export interface RankingResponse {
  scenario_id: string;
  strategies: StrategyResult[];
}
