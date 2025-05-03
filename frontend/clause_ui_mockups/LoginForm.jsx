import React, { useState } from "react";
import axios from "axios";
import { useAuth } from "./AuthContext";

function LoginForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useAuth();
  const [message, setMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const form = new FormData();
      form.append("username", username);
      form.append("password", password);

      const res = await axios.post("http://localhost:8000/login", form);
      login(res.data.access_token);
      setMessage("Login successful.");
    } catch (err) {
      setMessage("Login failed.");
    }
  };

  return (
    <div className="p-4 bg-white rounded shadow mb-6">
      <h2 className="text-lg font-bold mb-2">Login</h2>
      <form onSubmit={handleLogin} className="flex flex-col gap-3">
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" required className="border p-2 rounded" />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required className="border p-2 rounded" />
        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Login</button>
      </form>
      {message && <p className="mt-2 text-sm">{message}</p>}
    </div>
  );
}

export default LoginForm;
