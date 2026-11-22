
import { useState, useEffect } from 'react';
import { Image, Text, View, Button, FlatList } from 'react-native';
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
      const postsResponse = await fetch(`${BASE_URL}/api/profile/${PROFILE_ID}/posts`)
      const posts = await postsResponse.json();
      setPosts(posts.results);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <View style={styles.screen}>
      {profile && (
        <View style={styles.profile}>
          <Image source={{uri: profile.profile_image_url}} style={styles.profileImg}/>
          <Text style={styles.title}>{profile.display_name}</Text>
          <Text style={styles.contributor}>@{profile.username}</Text>
          <Text style={styles.text}>{profile.bio_text}</Text>
        </View>
      )}
      <Button title="Refresh" onPress={fetchData} />

      <FlatList
        style={styles.list}
        data={posts}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({item}) => (
          <View style={styles.inside}>
            {item.photo_set.map((photo) => (
              <Image
                key={photo.id}
                source={{uri: photo.image_url || photo.image_file || ''}}
                style={styles.image}
              />
            ))}
            <Text style={styles.text}>{item.caption}.</Text>
          </View>
        )}
      />

    </View>
  );
}