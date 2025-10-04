import React from 'react';
import EpisodeForm from './components/EpisodeForm';
import EpisodeList from './components/EpisodeList';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Podcast Generator</h1>
      </header>
      <main>
        <EpisodeForm />
        <EpisodeList />
      </main>
    </div>
  );
}

export default App;
