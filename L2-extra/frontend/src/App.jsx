// import { use, useState } from "react";
// import ReactMarkdown from "react-markdown";
// import AboutPage from "./pages/AboutPage";
// import { Link } from "react-router-dom";
// import "./App.css";

// function App() {
//   const [message, setMessage] = useState("");
//   const [response, setResponse] = useState("");
//   const [loading, setLoading] = useState(true);

//   async function sendMessage(params) {
//     setMessage("");
//     setLoading(true);
//     try {
//       console.log(message);
//       const res = await fetch("http://127.0.0.1:5000/chat", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify({ message }),
//       });
//       const data = await res.json();
//       console.log(data);
//       setResponse(data.response);
//     } catch (err) {
//       console.error(`Error During Fetching : ${err}`);
//       setResponse("Failed to get Response");
//     }

//     setLoading(false);
//   }

//   return (
//     <>
//       <div className="grid grid-cols-6 grid-rows-7 gap-3 bg-gray-700 h-screen w-screen">
//         <div className="col-span-4 row-span-3 col-start-2 row-start-2 bg-gray-600 whitespace-pre-wrap break-words overflow-auto p-4 text-white rounded-2xl">
//           <ReactMarkdown>{loading ? "Processing" : response}</ReactMarkdown>
//         </div>
//         <input
//           type="text"
//           placeholder="Ask Something..."
//           className="col-span-3 col-start-2 row-start-6 bg-gray-800 rounded-2xl pl-2.5 text-white"
//           value={message}
//           onChange={(e) => {
//             setMessage(e.target.value);
//           }}
//         />
//         <button
//           className="col-start-5 row-start-6 bg-gray-800 rounded-2xl text-gray-400 transition-colors
//          hover:bg-gray-600 duration-500"
//           onClick={sendMessage}
//         >
//           Send
//         </button>
//       </div>
//     </>
//   );
// }

// export default App;

import React from "react";
import AboutPage from "./pages/AboutPage";
import ChatPage from "./pages/ChatPage";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ChatPage />} />
        <Route path="/about" element={<AboutPage />} />
      </Routes>
    </Router>
  );
};

export default App;
