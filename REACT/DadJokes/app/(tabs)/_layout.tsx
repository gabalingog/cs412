// File: DadJokes/app/tabs/_layout.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/15/2026
// Description: Contains the base code, navigation

import { SymbolView } from 'expo-symbols';
import { Tabs } from 'expo-router';
import { Platform, Pressable } from 'react-native';

import Colors from '@/constants/Colors';
import { useColorScheme } from '@/components/useColorScheme';
import { useClientOnlyValue } from '@/components/useClientOnlyValue';

export default function TabLayout() {
  const colorScheme = useColorScheme();

  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: Colors[colorScheme].tint,
        headerShown: useClientOnlyValue(false, true),
      }}>
      <Tabs.Screen
        name="index"
        options={{
          title: 'Random Joke',
          tabBarIcon: ({ color }) => (
            <SymbolView
              name={{
                ios: 'face.smiling',
                android: 'mood',
                web: 'mood',
              }}
              tintColor={color}
              size={28}
            />
          ),
        }}
      />
      <Tabs.Screen
        name="jokes_list"
        options={{
          title: 'Jokes List',
          tabBarIcon: ({ color }) => (
            <SymbolView
              name={{
                ios: 'list.bullet',
                android: 'list',
                web: 'list',
              }}
              tintColor={color}
              size={28}
            />
          ),
        }}
      />
      <Tabs.Screen
        name="add_joke"
        options={{
          title: 'Add Joke',
          tabBarIcon: ({ color }) => (
            <SymbolView
              name={{
                ios: 'plus.circle',
                android: 'add_circle',
                web: 'add_circle',
              }}
              tintColor={color}
              size={28}
            />
          ),
        }}
      />
    </Tabs>
  );
}
