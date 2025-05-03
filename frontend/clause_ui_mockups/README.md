# Clause UI Mockups (Frontend)

This folder contains the React component mockups for clause suggestion and user interaction.

## Components

### `ClauseSuggestionBox.jsx`
A reusable UI component that:
- Displays suggested contract clauses
- Allows users to accept or reject a clause
- Uses Tailwind CSS utility classes for styling

## Usage

```jsx
import ClauseSuggestionBox from './ClauseSuggestionBox';

<ClauseSuggestionBox
  clause="This agreement shall be governed by the laws of Texas."
  onAccept={() => console.log('Accepted')}
  onReject={() => console.log('Rejected')}
/>
