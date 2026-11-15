import { useState, useEffect } from 'react';
import { ActivityIndicator, Text, View, FlatList } from 'react-native';
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
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchJokes = async () => {
    try {
      const response = await fetch(`${WEB_URL}/api/jokes`);
      const data = await response.json();
      setJokes(data.results);
    } catch (e) {
      console.log(e);
      setError(String(e))
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchJokes();
  }, []);

  if (loading) {
    return (
      <View style={styles.container}>
        <ActivityIndicator size="large" />
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.container}>
        <Text>{error}</Text>
      </View>
    );
  }

  return (
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
  );
}