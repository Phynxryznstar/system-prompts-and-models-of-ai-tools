// Mirrors api/models.py: ScenarioSummary and IngestionResult.

export interface ScenarioSummary {
  id: string;
  tax_year: number | null;
  filing_status: string | null;
  income_range: string | null;
  state: string | null;
  existing_elections: string[];
}

export interface IngestionResult {
  scenario_id: string;
  entities: number;
  activities: number;
  assets: number;
  constraints: number;
  state_tax_rules: number;
}

// Mirrors the nested objects in reasoning/scenario_schema.py's ClientScenario.
export interface ScenarioEntity {
  id: string;
  type: string;
  owner?: string | null;
  ownership_percent?: number | null;
  active_participation?: boolean | null;
}

export interface ScenarioActivity {
  id: string;
  type: string;
  entity: string;
  active?: boolean | null;
}

export interface ScenarioAsset {
  id: string;
  type: string;
  value?: number | null;
  acreage?: number | null;
  buildings?: number | null;
  activity?: string | null;
}

// The payload POST /scenario/ingest expects (mirrors ClientScenario).
export interface ClientScenarioPayload {
  id: string;
  tax_year: number;
  filing_status: string;
  income_range: string;
  state: string;
  entities: ScenarioEntity[];
  activities: ScenarioActivity[];
  assets: ScenarioAsset[];
  existing_elections: string[];
  constraints: string[];
}
