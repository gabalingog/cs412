// File: MiniInsta/feed.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/22/2026
// Description: Contains the posts of the profiles the user follows

import { useState, useEffect } from 'react';
import { Image, Text, View, Button, FlatList } from 'react-native';
import { styles } from '../../assets/my_styles';
import { BASE_URL } from '../constants/api';
import { useAuth } from '../context/AuthContext';

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

export default function FeedScreen() {
    const { authFetch, profileID } = useAuth();
    const [posts, setPosts] = useState<Post[]>([]);
    const fetchData = async () => {
        try {
            const response = await authFetch(`${BASE_URL}/api/profile/${profileID}/feed`);
            const data = await response.json();
            setPosts(data.results);
        } catch (e) {
            console.log(e);
        }
    };

    useEffect(() => {
        fetchData();
    }, []);

    return (
        <View style={styles.screen}>
            <Button title='Refresh' onPress={fetchData}/>
            <FlatList
                style={styles.list}
                data={posts}
                keyExtractor={(item) => item.id.toString()}
                renderItem={({item}) => (
                    <View style={styles.inside}>
                        {/* All posts of the followed users */}
                        {item.photo_set.map((photo) => (
                            <Image
                                key={photo.id}
                                source={{uri: photo.image_url || photo.image_file || ''}}
                                style={styles.image}
                            />
                        ))}
                        <Text style={styles.text}>{item.caption}</Text>
                    </View>
                )}
            />
        </View>
    );
}