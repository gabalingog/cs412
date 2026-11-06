// File: MyApp/assets/my_styles.ts
// Author: Gab Alingog (galingog@bu.edu), 11/06/2026
// Description: Contains the layout style of the app

import { StyleSheet } from 'react-native';

// Half came from the template that my React Native gave
export const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
    },
    title: {
      fontSize: 20,
      fontWeight: 'bold',
    },
    separator: {
      marginVertical: 30,
      height: 1,
      width: '80%',
    },
    // Started writing these by myself:
    text: {
      fontSize: 15,
      paddingHorizontal: 20,
      paddingVertical: 5,
    },
    image: {
      width: 250,
      height: 350,
      borderRadius: 10,
      padding: 5,
    },
    bold: {
      fontWeight: 'bold'
    },
    bullet: {
        fontSize: 20,
        fontWeight: 'bold',
        textAlign: 'left',
        alignSelf: 'flex-start',
        paddingHorizontal: 20,
        paddingVertical: 5,
    }
  });
  