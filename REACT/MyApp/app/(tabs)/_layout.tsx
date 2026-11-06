// File: MyApp/app/tabs/_layout.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/06/2026
// Description: Contains the base code, navigation

import { SymbolView } from 'expo-symbols';
import { Link, Tabs } from 'expo-router';
import { Platform, Pressable } from 'react-native';

import Colors from '@/constants/Colors';
import { useColorScheme } from '@/components/useColorScheme';
import { useClientOnlyValue } from '@/components/useClientOnlyValue';

// Majority of code came from the template that my Expo and React Native gave from starting
export default function TabLayout() {
  const colorScheme = useColorScheme();

  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: Colors[colorScheme].tint,
        // Disable the static render of the header on web
        // to prevent a hydration error in React Navigation v6.
        headerShown: useClientOnlyValue(false, true),
      }}>
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          // Home (index.tsx) tab
          tabBarIcon: ({ color }) => (
            <SymbolView
              name={{
                ios: 'house.fill', android: 'home', web: 'home'
              }}
              tintColor={color}
              size={28}
            />
          ),
          headerRight: () => (
            <Link href="/modal" asChild>
              <Pressable style={{ marginRight: 15 }}>
                {({ pressed }) => (
                  <SymbolView
                    name={{ ios: 'info.circle', android: 'info', web: 'info' }}
                    size={25}
                    tintColor={Colors[colorScheme].text}
                    style={{ opacity: pressed ? 0.5 : 1 }}
                  />
                )}
              </Pressable>
            </Link>
          ),
        }}
      />
      <Tabs.Screen
        name="detail"
        options={{
          title: 'Detail',
          // Details (detail.tsx) tab
          tabBarIcon: ({ color }) => (
            <SymbolView
            name={{
              ios: 'book.fill', android: 'menu_book', web: 'menu_book'
            }}
              tintColor={color}
              size={28}
            />
          ),
        }}
      />

      <Tabs.Screen
        name="about"
        options={{
          title: 'About',
          // About (about.tsx) tab
          tabBarIcon: ({ color }) => (
            <SymbolView
            name={{
              ios: 'person.fill', android: 'person', web: 'person'
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
