import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { getReport } from "../api/strategies";

interface ReportViewerProps {
  scenarioId: string;
}

type ReportViewerState =
  | { status: "loading" }
  | { status: "error"; message: string }
  | { status: "success"; markdown: string };

export default function ReportViewer({ scenarioId }: ReportViewerProps) {
  const [state, setState] = useState<ReportViewerState>({ status: "loading" });

  useEffect(() => {
    let cancelled = false;
    setState({ status: "loading" });

    getReport(scenarioId)
      .then((report) => {
        if (!cancelled) setState({ status: "success", markdown: report.markdown });
      })
      .catch((error: unknown) => {
        if (!cancelled) {
          setState({
            status: "error",
            message: error instanceof Error ? error.message : "Failed to load the report.",
          });
        }
      });

    return () => {
      cancelled = true;
    };
  }, [scenarioId]);

  if (state.status === "loading") {
    return <p className="text-sm text-slate-500">Loading report…</p>;
  }

  if (state.status === "error") {
    return <p className="text-sm text-red-600">{state.message}</p>;
  }

  return (
    <article className="prose prose-slate max-w-none rounded-xl border border-slate-200 bg-white p-8 shadow-sm">
      <ReactMarkdown remarkPlugins={[remarkGfm]}>{state.markdown}</ReactMarkdown>
    </article>
  );
}
