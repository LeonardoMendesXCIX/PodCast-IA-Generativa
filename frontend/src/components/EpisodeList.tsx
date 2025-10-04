import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Episode {
  id: number;
  title: string;
  status: string;
  audio_url?: string;
  image_url?: string;
}

const EpisodeList: React.FC = () => {
  const [episodes, setEpisodes] = useState<Episode[]>([]);

  useEffect(() => {
    const fetchEpisodes = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/episodes');
        setEpisodes(response.data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchEpisodes();
  }, []);

  return (
    <div>
      <h2>Your Episodes</h2>
      <ul>
        {episodes.map((episode) => (
          <li key={episode.id}>
            {episode.title} - {episode.status}
            {episode.audio_url && <a href={episode.audio_url}>Download Audio</a>}
            {episode.image_url && <img src={episode.image_url} alt="Cover" />}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EpisodeList;
