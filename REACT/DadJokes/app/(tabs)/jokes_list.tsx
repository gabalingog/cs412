// File: DadJokes/app/tabs/jokes_list.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/15/2026
// Description: List of all the jokes in the dataset

import { useState, useEffect } from 'react';
import { Text, View, FlatList, Button } from 'react-native';
import { styles } from '../../assets/my_styles';

const WEB_URL = 'https://cs-webapps.bu.edu/galingog/dadjokes';

type Joke = {
  id: number;
  text: string;
  name: string;
  timestamp: string;
};

export default function JokeListScreen() {
  const [jokes, setJokes] = useState<Joke[]>([]);

  const fetchJokes = async () => {
    try {
      const response = await fetch(`${WEB_URL}/api/jokes`);
      const data = await response.json();
      setJokes(data.results);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    fetchJokes();
  }, []);

  return (
    <View style={{flex: 1}}>
      <Button title="Refresh" onPress={fetchJokes} />
      <FlatList
        style={styles.list}
        data={jokes}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({item}) => (
          <View style={styles.inside}>
            <Text style={styles.jokeText}>{item.text}</Text>
            <Text style={styles.contributor}>by {item.name}</Text>
          </View>
        )}
      />
    </View>
  );
}