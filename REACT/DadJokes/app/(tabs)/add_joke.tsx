import { useState } from 'react';
import { Button, Text, TextInput, View } from 'react-native';
import { styles } from '../../assets/my_styles';

const WEB_URL = 'https://cs-webapps.bu.edu/galingog/dadjokes';

export default function AddJokeScreen() {
    const[text, setText] = useState('');
    const[name, setName] = useState('');
    const[message, setMessage] = useState('');

    const submitJoke = async () => {
        console.log('submitJoke:', {text, name});
        try {
            const response = await fetch(`${WEB_URL}/api/jokes`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                  },
                body: JSON.stringify({ text: text, name: name }),
        });

        console.log('submitJoke: ', response.status)

        if (response.status === 201) {
            const data = await response.json();
            console.log('submitJoke: created', data);
            setMessage('Joke added to list');
            setText('');
            setName('');
        } else {
            const errorData = await response.text();
            console.log('submitJoke: error', errorData);
            setMessage('Error, try again.')
        }
        } catch (e) {
            console.log('submitJoke: ', e);
            setMessage(String(e));
        }
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Add your joke:</Text>
            <TextInput
                style={styles.input}
                placeholder="Here..."
                value={text}
                onChangeText={setText}
                multiline
            />
            <Text style={styles.title}>Add your name:</Text>
            <TextInput
                style={styles.input}
                placeholder="Here..."
                value={name}
                onChangeText={setName}
            />

            <Button title='Submit' onPress={submitJoke} />
            {message !== '' && <Text style={styles.contributor}>{message}</Text>}
        </View>
    );
}
