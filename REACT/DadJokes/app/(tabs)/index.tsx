// File: DadJokes/app/tabs/index.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/15/2026
// Description: Show a random joke and picture

import { useState, useEffect } from 'react';
import { Image, Text, View, Button } from 'react-native';
import { styles } from '../../assets/my_styles';

// django website url
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

  const fetchData = async () => {
    try {
      const jokeResponse = await fetch(`${WEB_URL}/api/random`);
      setJoke(await jokeResponse.json());
      const pictureResponse = await fetch(`${WEB_URL}/api/random_picture`);
      setPicture(await pictureResponse.json());
    } catch (e) {
      console.log(e);
    }
  };

  // gets the data
  useEffect(() => {
    fetchData();
  }, []);

  return (
    // the joke and picture displayed
    <View style={styles.container}>
      <Text style={styles.title}>Dad Joke!</Text>
      {joke && <Text style={styles.jokeText}>{joke.text}</Text>}
      {joke && <Text style={styles.contributor}>Contributed by {joke.name}</Text>}
      {picture && (<Image source={{uri: picture.image_url}} style={styles.image}/>)}

      <Button title="New joke!" onPress={fetchData} />
    </View>
  );
}