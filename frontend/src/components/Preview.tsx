import React from 'react';

interface PreviewProps {
  episode: {
    title: string;
    script: string;
    audio_url?: string;
    image_url?: string;
  };
}

const Preview: React.FC<PreviewProps> = ({ episode }) => {
  return (
    <div>
      <h2>{episode.title}</h2>
      <p>{episode.script}</p>
      {episode.image_url && <img src={episode.image_url} alt="Cover" />}
      {episode.audio_url && <audio controls src={episode.audio_url} />}
    </div>
  );
};

export default Preview;
