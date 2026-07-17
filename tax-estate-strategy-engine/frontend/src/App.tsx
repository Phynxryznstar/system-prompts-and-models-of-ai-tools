import { BrowserRouter, Link, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Scenario from "./pages/Scenario";
import Report from "./pages/Report";

export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-full">
        <header className="border-b border-slate-200 bg-white">
          <div className="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
            <Link to="/" className="text-sm font-semibold tracking-tight text-slate-900">
              Tax + Estate Strategy Engine
            </Link>
          </div>
        </header>

        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/scenario/:id" element={<Scenario />} />
            <Route path="/scenario/:id/report" element={<Report />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}
