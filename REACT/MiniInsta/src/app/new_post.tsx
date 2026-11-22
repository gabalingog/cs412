
import { useState, useEffect } from 'react';
import { Image, Text, View, Button, FlatList, TextInput } from 'react-native';
import { styles } from '../../assets/my_styles';
import { BASE_URL, PROFILE_ID } from '../constants/api';


export default function PostScreen() {
    const [caption, setCaption] = useState('');
    const [imageUrl, setImageUrl] = useState('');

    const submitPost = async () => {
        const response = await fetch(`${BASE_URL}/api/profile/${PROFILE_ID}/posts`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({caption: caption, image_url: imageUrl}),
        });
        setCaption('');
        setImageUrl('');
    };
    
    return (
        <View style={styles.container}>
            <Text style={styles.title}>New Post:</Text>
            <TextInput
                style={styles.input}
                placeholder='Caption here...'
                value={caption}
                onChangeText={setCaption}
                multiline
            />

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