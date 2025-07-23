import {
  Bot,
  Zap,
  Code,
  Globe,
  AlertTriangle,
  Clock,
  Cpu,
  MessageSquare,
} from "lucide-react";

function AboutPage() {
  return (
    <div className="min-h-screen bg-black relative overflow-hidden">
      {/* Animated background */}
      <div className="absolute inset-0 bg-gradient-to-br from-gray-900 via-slate-800 to-gray-900"></div>
      <div className="absolute inset-0">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-orange-500/10 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-yellow-500/10 rounded-full blur-3xl animate-pulse delay-1000"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-orange-300/5 rounded-full blur-3xl animate-pulse delay-2000"></div>
      </div>

      <div className="relative z-10 container mx-auto px-6 py-12">
        {/* Header */}
        <div className="text-center mb-16">
          <div className="relative inline-block mb-6">
            <div className="w-20 h-20 bg-gradient-to-r from-orange-400 to-yellow-500 rounded-2xl flex items-center justify-center shadow-2xl shadow-orange-500/25 animate-pulse">
              <Bot className="w-10 h-10 text-black font-bold" />
            </div>
            <div className="absolute inset-0 w-20 h-20 bg-gradient-to-r from-orange-400 to-yellow-500 rounded-2xl blur-xl opacity-50 animate-ping"></div>
          </div>

          <h1 className="text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-yellow-500 mb-4">
            About LeetForce DSA Helper
          </h1>
          <p className="text-xl text-orange-300/80 max-w-3xl mx-auto leading-relaxed">
            Empower your coding journey with AI-enhanced problem solving.
            Designed to assist with Data Structures & Algorithms across
            interviews and platforms like LeetCode.
          </p>
        </div>

        {/* Feature Cards */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          <div className="bg-slate-800/60 border border-orange-500/30 rounded-2xl p-6 shadow-lg shadow-orange-500/20 hover:shadow-orange-500/30 transition-all duration-300 hover:scale-105">
            <div className="w-12 h-12 bg-gradient-to-r from-orange-400 to-yellow-400 rounded-lg flex items-center justify-center shadow-lg shadow-orange-400/50 mb-4">
              <Cpu className="w-6 h-6 text-black font-bold" />
            </div>
            <h3 className="text-xl font-bold text-white mb-2">
              Multi-Model Logic
            </h3>
            <p className="text-orange-300/80 leading-relaxed">
              Uses{" "}
              <span className="text-yellow-400 font-semibold">
                Google Gemini
              </span>{" "}
              &{" "}
              <span className="text-orange-400 font-semibold">OpenRouter</span>{" "}
              to power diverse AI conversations.
            </p>
          </div>

          <div className="bg-slate-800/60 border border-orange-500/30 rounded-2xl p-6 shadow-lg shadow-orange-500/20 hover:shadow-orange-500/30 transition-all duration-300 hover:scale-105">
            <div className="w-12 h-12 bg-gradient-to-r from-yellow-400 to-orange-500 rounded-lg flex items-center justify-center shadow-lg shadow-yellow-400/50 mb-4">
              <Code className="w-6 h-6 text-black font-bold" />
            </div>
            <h3 className="text-xl font-bold text-white mb-2">
              Built for Coders
            </h3>
            <p className="text-orange-300/80 leading-relaxed">
              Backend with{" "}
              <span className="text-yellow-400 font-semibold">FastAPI</span>,
              frontend in{" "}
              <span className="text-orange-400 font-semibold">
                React + Tailwind
              </span>
              .
            </p>
          </div>

          <div className="bg-slate-800/60 border border-orange-500/30 rounded-2xl p-6 shadow-lg shadow-orange-500/20 hover:shadow-orange-500/30 transition-all duration-300 hover:scale-105">
            <div className="w-12 h-12 bg-gradient-to-r from-orange-500 to-yellow-500 rounded-lg flex items-center justify-center shadow-lg shadow-orange-500/50 mb-4">
              <MessageSquare className="w-6 h-6 text-black font-bold" />
            </div>
            <h3 className="text-xl font-bold text-white mb-2">Rich Chat</h3>
            <p className="text-orange-300/80 leading-relaxed">
              Markdown-enabled responses, responsive design, and full chat
              history.
            </p>
          </div>
        </div>

        {/* Technical Section */}
        <div className="bg-slate-800/50 backdrop-blur-lg border border-orange-500/30 rounded-3xl p-8 mb-16 shadow-2xl shadow-orange-500/10">
          <h2 className="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-yellow-500 mb-8 text-center">
            How It Works
          </h2>

          <div className="grid md:grid-cols-2 gap-8">
            <div>
              <h3 className="text-xl font-bold text-white mb-4 flex items-center">
                <Globe className="w-5 h-5 mr-2 text-orange-400" />
                API Logic
              </h3>
              <ul className="space-y-3 text-orange-300/80">
                <li className="flex items-start">
                  <div className="w-2 h-2 bg-orange-400 rounded-full mt-2 mr-3" />
                  <span>
                    <strong className="text-white">Gemini API:</strong> Natural
                    language reasoning and analysis
                  </span>
                </li>
                <li className="flex items-start">
                  <div className="w-2 h-2 bg-yellow-400 rounded-full mt-2 mr-3" />
                  <span>
                    <strong className="text-white">OpenRouter:</strong>{" "}
                    Randomized model validation layer
                  </span>
                </li>
                <li className="flex items-start">
                  <div className="w-2 h-2 bg-orange-200 rounded-full mt-2 mr-3" />
                  <span>
                    <strong className="text-white">SDKs:</strong> Secure,
                    production-ready integration
                  </span>
                </li>
              </ul>
            </div>

            <div>
              <h3 className="text-xl font-bold text-white mb-4 flex items-center">
                <Code className="w-5 h-5 mr-2 text-yellow-400" />
                Developer Stack
              </h3>
              <ul className="space-y-3 text-orange-300/80">
                <li className="flex items-start">
                  <div className="w-2 h-2 bg-orange-400 rounded-full mt-2 mr-3" />
                  <span>
                    <strong className="text-white">Backend:</strong> Python +
                    FastAPI
                  </span>
                </li>
                <li className="flex items-start">
                  <div className="w-2 h-2 bg-yellow-400 rounded-full mt-2 mr-3" />
                  <span>
                    <strong className="text-white">Frontend:</strong> React with
                    hooks and modular components
                  </span>
                </li>
                <li className="flex items-start">
                  <div className="w-2 h-2 bg-orange-200 rounded-full mt-2 mr-3" />
                  <span>
                    <strong className="text-white">Styling:</strong> Tailwind
                    CSS with DSA-themed dark UI
                  </span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        {/* Disclaimers */}
        <div className="bg-gradient-to-r from-yellow-500/20 to-orange-500/20 border border-yellow-500/30 rounded-2xl p-6 shadow-lg shadow-yellow-500/20">
          <div className="flex items-start space-x-4">
            <div className="w-12 h-12 bg-gradient-to-r from-yellow-400 to-orange-500 rounded-lg flex items-center justify-center shadow-lg shadow-yellow-500/50">
              <AlertTriangle className="w-6 h-6 text-black font-bold" />
            </div>
            <div>
              <h3 className="text-xl font-bold text-white mb-3">
                Disclaimer & Caution
              </h3>
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="text-lg font-semibold text-yellow-300 mb-2 flex items-center">
                    <Clock className="w-4 h-4 mr-2" />
                    Response Latency
                  </h4>
                  <p className="text-yellow-200/80 text-sm leading-relaxed">
                    Free tier APIs may take time or timeout under heavy load.
                  </p>
                </div>
                <div>
                  <h4 className="text-lg font-semibold text-orange-300 mb-2 flex items-center">
                    <Zap className="w-4 h-4 mr-2" />
                    Accuracy Disclaimer
                  </h4>
                  <p className="text-orange-200/80 text-sm leading-relaxed">
                    Always verify results from the bot, especially in interviews
                    or exams.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="text-center mt-16">
          <p className="text-orange-300/60 text-sm">
            Built for DSA aspirants • Powered by AI • Theme: LeetCode Dark
          </p>
          <div className="flex items-center justify-center space-x-4 mt-4">
            <div className="w-8 h-8 bg-gradient-to-r from-orange-400 to-yellow-500 rounded-lg flex items-center justify-center opacity-70">
              <Bot className="w-4 h-4 text-black" />
            </div>
            <span className="text-xs text-orange-300/40">
              LeetCode DSA Solver v1.0
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AboutPage;
