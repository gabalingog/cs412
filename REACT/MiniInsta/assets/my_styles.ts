import { StyleSheet } from "react-native";

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
    text: { 
      fontSize: 18, 
      textAlign: 'center', 
      marginBottom: 8, 
    },
    contributor: {
      fontSize: 14, 
      color: 'gray', 
      marginBottom: 20,
    },
    image: {
      width: 300, 
      height: 300, 
      borderRadius: 10,
    },
    list: {
        flex: 1,
        paddingHorizontal: 15,
    },
    inside: {
        paddingVertical: 15,
        borderBottomWidth: 1,
        borderBottomColor: '#ddd'
    },
    input: {
        width: '90%',
        borderWidth: 1,
        borderColor: '#ddd',
        borderRadius: 5,
        padding: 10,
        marginBottom: 10,
        fontSize: 15,
    }
  });
  