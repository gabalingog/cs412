// File: MiniInsta/new_post.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/22/2026
// Description: Create a new post for the user

import { useState, useEffect } from 'react';
import { Image, Text, View, Button, FlatList, TextInput } from 'react-native';
import { styles } from '../../assets/my_styles';
import { BASE_URL } from '../constants/api';
import { useAuth } from '../context/AuthContext';


export default function PostScreen() {
    const { authFetch, profileID } = useAuth();
    const [caption, setCaption] = useState('');
    const [imageUrl, setImageUrl] = useState('');

    const submitPost = async () => {
        const response = await authFetch(`${BASE_URL}/api/profile/${profileID}/posts`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({caption: caption, image_url: imageUrl}),
        });
        setCaption('');
        setImageUrl('');
    };
    
    return (
        <View style={styles.container}>
            {/* Post */}
            <Text style={styles.title}>New Post:</Text>
            <TextInput
                style={styles.input}
                placeholder='Caption here...'
                value={caption}
                onChangeText={setCaption}
                multiline
            />

            {/* Only accepts url for image */}
            <Text style={styles.title}>Image (optional):</Text>
            <TextInput
                style={styles.input}
                placeholder='Image URL here...'
                value={imageUrl}
                onChangeText={setImageUrl}
            />
            <Button title='Post' onPress={submitPost}/>
        </View>
    );
}