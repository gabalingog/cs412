
import { useState, useEffect } from 'react';
import { Image, Text, View, Button, FlatList } from 'react-native';
import { styles } from '../../assets/my_styles';
import { BASE_URL, PROFILE_ID } from '../constants/api';

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
    const [posts, setPosts] = useState<Post[]>([]);
    const fetchData = async () => {
        try {
            const response = await fetch(`${BASE_URL}/api/profile/${PROFILE_ID}/feed`);
            const data = await response.json();
            setPosts(data.results);
        } catch (e) {
            console.log(e);
        }
    };

    useEffect(() => {
        fetchData();
    }, []);

    
}