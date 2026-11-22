// File: MiniInsta/new_post.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/22/2026
// Description: Login page of the app

import { useState } from 'react';
import { Button, Text, TextInput, View } from 'react-native';
import { styles } from '../../assets/my_styles';
import { useAuth } from '../context/AuthContext';

export default function LoginScreen() {
  const {login} = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  return (
    <View style={styles.container}>
        {/* Username text */}
      <Text style={styles.title}>Login</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
      />
      {/* Password text */}
      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Login" onPress={() => login(username, password)} />
    </View>
  );
}