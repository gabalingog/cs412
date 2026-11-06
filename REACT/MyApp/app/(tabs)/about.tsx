// File: MyApp/app/tabs/about.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/06/2026
// Description: About page of the app with more information

import { StyleSheet, Image } from 'react-native';
import { Text, View } from '@/components/Themed';
import { styles } from '../../assets/my_styles';

// Styles are imported from assets

export default function AboutScreen() {
  return (
    <View style={styles.container}>
        <Text style={styles.title}>About</Text>
        <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
        {/* Simple text and image from assets */}
        <Text style={styles.text}>
            Thank you for visiting my app! Here's a screenshot from my personal portfolio website.
        </Text>
        <Image
          source={{uri: 'https://cs-people.bu.edu/galingog/gab.png'}}
          style={styles.image}
        />
    </View>
  );
}