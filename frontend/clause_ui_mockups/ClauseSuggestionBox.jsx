import React from "react";

function ClauseSuggestionBox({ clause, onAccept, onReject }) {
  return (
    <div className="p-4 border rounded shadow mb-2 bg-white">
      <p className="text-sm text-gray-600 font-medium">Suggested Clause:</p>
      <pre className="whitespace-pre-wrap text-sm text-black bg-gray-100 p-2 rounded">
        {clause}
      </pre>
      <div className="mt-2 flex gap-2">
        <button
          onClick={onAccept}
          className="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600"
        >
          Accept
        </button>
        <button
          onClick={onReject}
          className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
        >
          Reject
        </button>
      </div>
    </div>
  );
}

export default ClauseSuggestionBox;
