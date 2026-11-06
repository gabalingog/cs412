// File: MyApp/app/tabs/detail.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/06/2026
// Description: Detailed view of interests with images

import { ScrollView, Image } from 'react-native';
import { Text, View } from '@/components/Themed';
import { styles } from '../../assets/my_styles';

// Styles are imported from assets

export default function DetailScreen() {
  return (
    <ScrollView>
      <View style={styles.container}>
        <Text style={styles.title}>Detail</Text>
        <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
        <Text style={styles.text}>
          Here are a list of my interests outside of academics!
        </Text>
        {/* Created a new style for bullet points */}
        <Text style={styles.bullet}>
          1. Reading
        </Text>
        {/* Simple text and the image is from an external source */}
        <Text style={styles.text}>
          In my free time, I read alot of classics such as Jane Austen. However, my favorite book is 
          The Secret History which I read every year.
        </Text>
        <Image
          source={{uri: 'https://cs-people.bu.edu/galingog/cs1.jpg'}}
          style={styles.image}
        />

        <Text style={styles.bullet}>
          2. Learn new languages
        </Text>
        <Text style={styles.text}>
          Right now, I am taking courses to learn Spanish, which is the parent language of what I am fluent in, Tagalog (Filipino).
          My goal in life is to work remotely and travel the world, hence my next language after Spanish is hopefully Japanese.
        </Text>
        <Image
          source={{uri: 'https://cs-people.bu.edu/galingog/img.jpeg'}}
          style={styles.image}
        />
      </View>
    </ScrollView>
  );
}