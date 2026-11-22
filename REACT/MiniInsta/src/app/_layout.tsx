// File: MiniInsta/_layout.tsx
// Author: Gab Alingog (galingog@bu.edu), 11/22/2026
// Description: Contains the base code, navigation

import { DarkTheme, DefaultTheme, ThemeProvider, Tabs } from 'expo-router';
import { SymbolView } from 'expo-symbols';
import * as SplashScreen from 'expo-splash-screen';
import { useColorScheme } from 'react-native';

import { AnimatedSplashOverlay } from '@/components/animated-icon';

SplashScreen.preventAutoHideAsync();

export default function TabLayout() {
  const colorScheme = useColorScheme();
  return (
    <ThemeProvider value={colorScheme === 'dark' ? DarkTheme : DefaultTheme}>
      <AnimatedSplashOverlay />
      <Tabs screenOptions={{ headerShown: false }}>
        <Tabs.Screen
          name="index"
          options={{
            title: 'Profile',
            tabBarIcon: ({ color }) => (
              <SymbolView
                name={{
                  ios: 'person',
                  android: 'person',
                  web: 'person',
                }}
                tintColor={color}
                size={28}
              />
            ),
          }}
        />
        <Tabs.Screen
          name="feed"
          options={{
            title: 'Feed',
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
          name="new_post"
          options={{
            title: 'New Post',
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
    </ThemeProvider>
  );
}