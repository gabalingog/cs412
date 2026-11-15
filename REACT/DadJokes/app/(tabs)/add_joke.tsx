// File: DadJokes/app/tabs/add_joke.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/15/2026
// Description: Add a joke to the dataset

import { useState } from 'react';
import { Button, Text, TextInput, View } from 'react-native';
import { styles } from '../../assets/my_styles';

const WEB_URL = 'https://cs-webapps.bu.edu/galingog/dadjokes';

export default function AddJokeScreen() {
    const[text, setText] = useState('');
    const[name, setName] = useState('');

    // sends the joke to the django REST API with POST
    const submitJoke = async () => {
        console.log('submitJoke:', {text, name});
        const response = await fetch(`${WEB_URL}/api/jokes`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                },
            body: JSON.stringify({ text: text, name: name }),
        });

        // debut HTTP
        console.log('submitJoke: ', response.status)
        setText('');
        setName('');
    };

    return (
        <View style={styles.container}>
            {/* input for the text joke */}
            <Text style={styles.title}>Add your joke:</Text>
            <TextInput
                style={styles.input}
                placeholder="Here..."
                value={text}
                onChangeText={setText}
                multiline
            />
            {/* input for the name */}
            <Text style={styles.title}>Add your name:</Text>
            <TextInput
                style={styles.input}
                placeholder="Here..."
                value={name}
                onChangeText={setName}
            />

            {/* submit button */}
            <Button title='Submit' onPress={submitJoke} />
        </View>
    );
}
