import React, { useState } from 'react';
import axios from 'axios';

const EpisodeForm: React.FC = () => {
  const [title, setTitle] = useState('');
  const [prompt, setPrompt] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/v1/episodes', { title, prompt });
      alert(`Episode created with ID: ${response.data.episode_id}`);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Episode Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        placeholder="Prompt for script"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button type="submit">Generate Episode</button>
    </form>
  );
};

export default EpisodeForm;
