import React, { useState } from "react";
import axios from "axios";

function ClauseSubmitForm() {
  const [form, setForm] = useState({
    user_id: "",
    title: "",
    content: "",
    document_type: "contract",
    jurisdiction: "US",
    edited: false,
    accepted: false
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:8000/clause/submit", form);
      setMessage("Clause submitted successfully! ID: " + res.data.clause_id);
    } catch (err) {
      setMessage("Error submitting clause.");
    }
  };

  return (
    <div className="p-4 max-w-xl mx-auto bg-white rounded shadow">
      <h2 className="text-lg font-bold mb-2">Submit Clause</h2>
      <form onSubmit={handleSubmit} className="flex flex-col gap-3">
        <input name="user_id" value={form.user_id} onChange={handleChange} placeholder="User ID" required className="border p-2 rounded" />
        <input name="title" value={form.title} onChange={handleChange} placeholder="Clause Title" required className="border p-2 rounded" />
        <textarea name="content" value={form.content} onChange={handleChange} placeholder="Clause Content" required className="border p-2 rounded" />
        <input name="document_type" value={form.document_type} onChange={handleChange} placeholder="Document Type" className="border p-2 rounded" />
        <input name="jurisdiction" value={form.jurisdiction} onChange={handleChange} placeholder="Jurisdiction" className="border p-2 rounded" />
        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Submit</button>
      </form>
      {message && <p className="mt-4 text-sm text-green-700">{message}</p>}
    </div>
  );
}

export default ClauseSubmitForm;
