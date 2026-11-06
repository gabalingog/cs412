// File: MyApp/app/tabs/index.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/06/2026
// Description: Home page of the app

import { StyleSheet, Image } from 'react-native';
import { Text, View } from '@/components/Themed';
import { styles } from '../../assets/my_styles';

// Styles are imported from assets

export default function IndexScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Gab Alingog</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      {/* Simple text and the image is from an external source */}
      <Text style={styles.text}>
        <Text style={styles.bold}>Hello!</Text> I am a junior studying CS & Math in BU. I live in California and the Philippines.
        On campus, I am invovled in Hack4Impact, Girls Who Code, and AKPsi. Personally, I like to read and aspire to learn new languages.
      </Text>
      <Image
        source={require('../../assets/images/AKPsi Headshot.png')} 
        style={styles.image}
      />
    </View>
  );
}