import { useState, useEffect } from 'react';
import { ActivityIndicator, Image, Text, View, Button } from 'react-native';
import { styles } from '../../assets/my_styles';

const WEB_URL = 'https://cs-webapps.bu.edu/galingog/dadjokes';

type Joke = {
  id: number;
  text: string;
  name: string;
  timestamp: string;
};

type Picture = {
  id: number;
  image_url: string;
  name: string;
  timestamp: string;
}

export default function IndexScreen() {
  const [joke, setJoke] = useState<Joke | null>(null);
  const [picture, setPicture] = useState<Picture | null>(null);
  const [error, setError] = useState<string | null>(null);

  const fetchData = async () => {
    setError(null);
    setJoke(null);
    setPicture(null);
    try {
      const jokeResponse = await fetch(`${WEB_URL}/api/random`);
      const jokeData = await jokeResponse.json();
      setJoke(jokeData);
      const pictureResponse = await fetch(`${WEB_URL}/api/random_picture`);
      const pictureData = await pictureResponse.json();
      setPicture(pictureData);
    } catch (e) {
      // setError('Error');
      console.log(e);
      setError(String(e));
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  if (error) {
    return (
      <View style={styles.container}>
        <Text>{error}</Text>
      </View>
    );
  }

  if (!joke || !picture) {
    return (
      <View style={styles.container}>
        <ActivityIndicator size="large" />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Dad Joke!</Text>
      <Text style={styles.jokeText}>{joke.text}</Text>
      <Text style={styles.contributor}>Contributed by {joke.name}</Text>
      <Image source={{uri: picture.image_url}} style={styles.image}/>

      <Button title="New joke!" onPress={fetchData} />
    </View>
  );
}