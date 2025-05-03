import React from "react";
import { AuthProvider, useAuth } from "./AuthContext";
import RegisterForm from "./RegisterForm";
import LoginForm from "./LoginForm";
import ClauseSubmitForm from "./ClauseSubmitForm";
import ClauseSuggestionBox from "./ClauseSuggestionBox";

function MainContent() {
  const { token } = useAuth();

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-2xl font-bold text-center mb-6">Clause Engine UI</h1>
      <RegisterForm />
      <LoginForm />
      {token && (
        <>
          <ClauseSubmitForm />
          <hr className="my-6" />
          <ClauseSuggestionBox
            clause="This agreement is governed by the laws of Texas."
            onAccept={() => alert("Accepted!")}
            onReject={() => alert("Rejected!")}
          />
        </>
      )}
    </div>
  );
}

function App() {
  return (
    <AuthProvider>
      <MainContent />
    </AuthProvider>
  );
}

export default App;
