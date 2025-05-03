import React from "react";
import ClauseSubmitForm from "./ClauseSubmitForm";
import ClauseSuggestionBox from "./ClauseSuggestionBox";

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-2xl font-bold text-center mb-6">Clause Engine UI</h1>
      <ClauseSubmitForm />
      <hr className="my-6" />
      <ClauseSuggestionBox
        clause="This agreement is governed by the laws of Texas."
        onAccept={() => alert("Accepted!")}
        onReject={() => alert("Rejected!")}
      />
    </div>
  );
}

export default App;
