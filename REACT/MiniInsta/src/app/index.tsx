
import { useState, useEffect } from 'react';
import { Image, Text, View, Button } from 'react-native';
import { styles } from '../../assets/my_styles';
import { BASE_URL, PROFILE_ID } from '../constants/api';

type Profile = {
  id: number;
  username: string;
  display_name: string;
  bio_text: string;
  profile_image_url: string;
  join_date: string;
};

type Photo = {
  id: number;
  image_url: string;
  image_file: string | null;
  timestamp: string;
};

type Post = {
  id: number,
  caption: string,
  timestamp: string;
  photo_set: Photo[];
};

export default function ProfileScreen() {
  const [profile, setProfile] = useState<Profile | null>(null);
  const [posts, setPosts] = useState<Post[]>([]);

  const fetchData = async () => {
    try {
      const profileResponse = await fetch(`${BASE_URL}/api/profile/${PROFILE_ID}`);
      setProfile(await profileResponse.json());
    }
  }
}