import React, { useRef, useState, useEffect } from "react";
import {
  Code2,
  User,
  Loader2,
  Terminal,
  Send,
  Zap,
  BookOpen,
  Target,
  Github,
  ExternalLink,
  Linkedin,
} from "lucide-react";

function ChatPage() {
  const [message, setMessage] = useState("");
  const [conversations, setConversations] = useState([]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [conversations]);

  async function sendMessage() {
    if (!message.trim() || loading) return;

    const userMessage = message.trim();
    setMessage("");

    // Add user message to conversation
    const newUserMessage = {
      id: Date.now(),
      type: "user",
      content: userMessage,
      timestamp: new Date(),
    };

    setConversations((prev) => [...prev, newUserMessage]);
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userMessage }),
      });

      const data = await res.json();

      // Add bot response to conversation
      const botMessage = {
        id: Date.now() + 1,
        type: "bot",
        content: data.response,
        timestamp: new Date(),
      };

      setConversations((prev) => [...prev, botMessage]);
    } catch (err) {
      console.error(`Error During Fetching: ${err}`);
      const errorMessage = {
        id: Date.now() + 1,
        type: "bot",
        content:
          "I'm sorry, Something went wrong while processing your request. It looks like all tokens may have been used. Please try again shortly or refresh the page to continue.",
        timestamp: new Date(),
        isError: true,
      };
      setConversations((prev) => [...prev, errorMessage]);
    }

    setLoading(false);
  }

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const formatTime = (date) => {
    return date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  };

  return (
    <div className="flex flex-col h-screen bg-gradient-to-br from-gray-900 via-slate-800 to-gray-900">
      {/* Header */}
      <div className="bg-slate-800/90 backdrop-blur-md border-b border-orange-500/30 px-6 py-4">
        <div className="flex items-center space-x-3 justify-between">
          {/* Left Side - Logo and Text */}
          <div className="relative flex">
            <div className="bg-gradient-to-r from-orange-500 to-yellow-500 p-2 rounded-lg mr-3">
              <Code2 className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold text-white flex items-center">
                LeetForce
                <Zap className="w-5 h-5 text-yellow-400 ml-2" />
              </h1>
              <p className="text-sm text-orange-300">Your DSA prep companion</p>
            </div>
          </div>

          {/* Right Side - Links */}
          <div className="flex items-center space-x-3">
            <a
              href="https://github.com/your-username"
              target="_blank"
              rel="noopener noreferrer"
              title="GitHub"
            >
              <Github className="w-5 h-5 text-orange-300 hover:text-orange-100 transition-colors duration-150" />
            </a>
            <a
              href="https://linkedin.com/in/your-profile"
              target="_blank"
              rel="noopener noreferrer"
              title="LinkedIn"
            >
              <Linkedin className="w-5 h-5 text-orange-300 hover:text-orange-100 transition-colors duration-150" />
            </a>
            <a
              href="https://cgc-unite.vercel.app"
              target="_blank"
              rel="noopener noreferrer"
              title="CGC Unite"
            >
              {/* <ExternalLink className="w-5 h-5 text-orange-300 hover:text-orange-100 transition-colors duration-150" /> */}
              <p className="text-orange-300 hover:text-orange-100 transition-colors duration-150">
                CGC-Unite
              </p>
            </a>
            <a href="/about" style={{ textDecoration: "none" }}>
              <div className="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-orange-300 hover:text-orange-200 rounded-lg transition-all duration-200 font-medium border border-orange-500/20">
                About
              </div>
            </a>
          </div>
        </div>
      </div>

      {/* Messages Container */}
      <div className="flex-1 overflow-hidden">
        <div className="h-full overflow-y-auto px-4 py-6">
          {conversations.length === 0 ? (
            <div className="flex flex-col items-center justify-center h-full text-center">
              <div className="bg-gradient-to-r from-orange-500 to-yellow-500 p-6 rounded-2xl mb-6 shadow-2xl">
                <Terminal className="w-16 h-16 text-white" />
              </div>
              <h2 className="text-3xl font-bold text-white mb-4">
                Welcome to LeetForce! 🚀
              </h2>
              <p className="text-orange-300 max-w-2xl mb-6 text-lg">
                Get instant help with Data Structures & Algorithms problems. Ask
                about solutions, time complexity, coding patterns, or any
                LeetCode question!
              </p>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-3xl">
                <div className="bg-slate-800/50 backdrop-blur-sm border border-orange-500/20 rounded-xl p-4">
                  <BookOpen className="w-8 h-8 text-orange-400 mb-2 mx-auto" />
                  <h3 className="text-white font-semibold mb-1">
                    Problem Analysis
                  </h3>
                  <p className="text-gray-400 text-sm">
                    Break down complex problems step by step
                  </p>
                </div>

                <div className="bg-slate-800/50 backdrop-blur-sm border border-orange-500/20 rounded-xl p-4">
                  <Code2 className="w-8 h-8 text-orange-400 mb-2 mx-auto" />
                  <h3 className="text-white font-semibold mb-1">
                    Solution Patterns
                  </h3>
                  <p className="text-gray-400 text-sm">
                    Learn common coding patterns and techniques
                  </p>
                </div>

                <div className="bg-slate-800/50 backdrop-blur-sm border border-orange-500/20 rounded-xl p-4">
                  <Target className="w-8 h-8 text-orange-400 mb-2 mx-auto" />
                  <h3 className="text-white font-semibold mb-1">
                    Optimization Tips
                  </h3>
                  <p className="text-gray-400 text-sm">
                    Improve time & space complexity
                  </p>
                </div>
              </div>

              <div className="mt-8 text-orange-400/80 text-sm">
                💡 Try asking: "Explain the Two Sum problem" or "Best approach
                for binary tree traversal"
              </div>
            </div>
          ) : (
            <div className="space-y-4 max-w-4xl mx-auto">
              {conversations.map((conv) => (
                <div
                  key={conv.id}
                  className={`flex ${
                    conv.type === "user" ? "justify-end" : "justify-start"
                  }`}
                >
                  <div
                    className={`flex items-start space-x-3 max-w-3xl ${
                      conv.type === "user"
                        ? "flex-row-reverse space-x-reverse"
                        : ""
                    }`}
                  >
                    {/* Avatar */}
                    <div
                      className={`flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center ${
                        conv.type === "user"
                          ? "bg-gradient-to-r from-orange-500 to-yellow-500"
                          : conv.isError
                          ? "bg-red-500"
                          : "bg-gradient-to-r from-orange-500 to-yellow-500"
                      }`}
                    >
                      {conv.type === "user" ? (
                        <User className="w-5 h-5 text-white" />
                      ) : (
                        <Code2 className="w-5 h-5 text-white" />
                      )}
                    </div>

                    {/* Message Bubble */}
                    <div
                      className={`px-4 py-3 rounded-2xl ${
                        conv.type === "user"
                          ? "bg-gradient-to-r from-orange-500 to-yellow-800 text-white shadow-lg"
                          : conv.isError
                          ? "bg-red-500/20 border border-red-500/30 text-red-300"
                          : "bg-slate-800/70 backdrop-blur-sm border border-orange-500/20 text-white shadow-lg"
                      }`}
                    >
                      <div className="whitespace-pre-wrap break-words prose prose-invert max-w-none">
                        {conv.type === "user" ? (
                          conv.content
                        ) : (
                          <div
                            dangerouslySetInnerHTML={{
                              __html: conv.content
                                .replace(
                                  /```(\w+)?\n([\s\S]*?)```/g,
                                  '<pre class="bg-slate-900 border border-orange-500/30 rounded-lg p-3 overflow-x-auto my-2"><code class="text-orange-200">$2</code></pre>'
                                )
                                .replace(
                                  /`([^`]+)`/g,
                                  '<code class="bg-slate-900 text-orange-300 px-1 py-0.5 rounded text-sm">$1</code>'
                                )
                                .replace(
                                  /\*\*(.*?)\*\*/g,
                                  '<strong class="text-orange-200">$1</strong>'
                                )
                                .replace(
                                  /\*(.*?)\*/g,
                                  '<em class="text-orange-300">$1</em>'
                                )
                                .replace(/\n/g, "<br>"),
                            }}
                          />
                        )}
                      </div>
                      <div
                        className={`text-xs mt-2 opacity-70 ${
                          conv.type === "user"
                            ? "text-white"
                            : "text-orange-300"
                        }`}
                      >
                        {formatTime(conv.timestamp)}
                      </div>
                    </div>
                  </div>
                </div>
              ))}

              {/* Loading indicator */}
              {loading && (
                <div className="flex justify-start">
                  <div className="flex items-start space-x-3 max-w-3xl">
                    <div className="flex-shrink-0 w-10 h-10 rounded-full bg-gradient-to-r from-orange-500 to-yellow-500 flex items-center justify-center">
                      <Code2 className="w-5 h-5 text-white" />
                    </div>
                    <div className="bg-slate-800/70 backdrop-blur-sm border border-orange-500/20 px-4 py-3 rounded-2xl">
                      <div className="flex items-center space-x-2 text-orange-300">
                        <Loader2 className="w-4 h-4 animate-spin" />
                        <span>Analyzing problem...</span>
                      </div>
                    </div>
                  </div>
                </div>
              )}

              <div ref={messagesEndRef} />
            </div>
          )}
        </div>
      </div>

      {/* Input Area */}
      <div className="bg-slate-800/90 backdrop-blur-md border-t border-orange-500/30 p-4">
        <div className="max-w-4xl mx-auto">
          <div className="relative flex items-end space-x-3">
            <div className="flex-1 relative">
              <textarea
                ref={inputRef}
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Ask about any LeetCode problem, algorithm, or data structure... (Enter to send, Shift+Enter for new line)"
                className="w-full bg-slate-900/80 backdrop-blur-sm border border-orange-500/30 rounded-2xl px-4 py-3 pr-12 text-white placeholder-orange-300/70 resize-none focus:outline-none focus:ring-2 focus:ring-orange-400 focus:border-orange-400 transition-all duration-200 min-h-[48px] max-h-32"
                rows={1}
                disabled={loading}
              />
            </div>

            <button
              onClick={sendMessage}
              disabled={!message.trim() || loading}
              className="bg-gradient-to-r from-orange-500 to-yellow-500 hover:from-orange-600 hover:to-yellow-600 disabled:from-gray-600 disabled:to-gray-600 text-white p-3 rounded-2xl transition-all duration-200 disabled:cursor-not-allowed disabled:opacity-50 transform hover:scale-105 active:scale-95 shadow-lg"
            >
              {loading ? (
                <Loader2 className="w-5 h-5 animate-spin" />
              ) : (
                <Send className="w-5 h-5" />
              )}
            </button>
          </div>

          <div className="flex items-center justify-center mt-2">
            <p className="text-xs text-orange-400/70">
              🎯 Specialized for LeetCode DSA problems • Solutions may require
              verification
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ChatPage;
