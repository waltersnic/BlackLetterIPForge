import React, { useState } from "react";
import axios from "axios";

function RegisterForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:8000/register", {
        username,
        password,
      });
      setMessage("Registered successfully. You may now log in.");
    } catch (err) {
      setMessage("Registration failed.");
    }
  };

  return (
    <div className="p-4 bg-white rounded shadow mb-6">
      <h2 className="text-lg font-bold mb-2">Register</h2>
      <form onSubmit={handleRegister} className="flex flex-col gap-3">
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" required className="border p-2 rounded" />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required className="border p-2 rounded" />
        <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded">Register</button>
      </form>
      {message && <p className="mt-2 text-sm">{message}</p>}
    </div>
  );
}

export default RegisterForm;
