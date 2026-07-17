import { Link, useParams } from "react-router-dom";
import ReportViewer from "../components/ReportViewer";

export default function Report() {
  const { id } = useParams<{ id: string }>();

  if (!id) {
    return <p className="p-6 text-sm text-red-600">No scenario id provided.</p>;
  }

  return (
    <div className="mx-auto max-w-4xl px-6 py-12">
      <div className="mb-6 flex items-center justify-between">
        <h1 className="text-2xl font-bold text-slate-900">Strategy Report</h1>
        <Link to={`/scenario/${id}`} className="text-sm font-medium text-slate-600 hover:text-slate-900">
          &larr; Back to scenario
        </Link>
      </div>
      <ReportViewer scenarioId={id} />
    </div>
  );
}
