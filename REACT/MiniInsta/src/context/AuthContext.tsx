// File: MiniInsta/AuthContext.tsx
// // Author: Gab Alingog (galingog@bu.edu), 11/22/2026
// Description: Authentication for the app

import { createContext, useContext, useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { BASE_URL } from '../constants/api';

const AuthContext = createContext<any>(null);

export function AuthProvider({children}: {children: React.ReactNode}) {
    const [token, setToken] = useState<string | null>(null);
    const [profileID, setProfileID] = useState<string | null>(null);

    useEffect(() => {
        (async () => {
            setToken(await AsyncStorage.getItem('auth_token'));
            setProfileID(await AsyncStorage.getItem('profile_id'));
        })();
    }, []);

    const login = async (username: string, password: string) => {
        const resp = await fetch(`${BASE_URL}/api/login`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username: username, password: password}),
        });
        // Login successful
        console.log(resp.status);
        if (resp.status == 200) {
            const data = await resp.json()
            await AsyncStorage.setItem('auth_token', data.token);
            await AsyncStorage.setItem('profile_id', String(data.profile.id));
            setToken(data.token);
            setProfileID(String(data.profile.id));
        }
    };

    // Logout of app
    const logout = async () => {
        await AsyncStorage.removeItem('auth_token');
        await AsyncStorage.removeItem('profile_id');
        setToken(null);
        setProfileID(null);
    };

    // Adds token authentication
    const authFetch = async (url: string, options: RequestInit = {}) => {
        const resp = await fetch(url, { ...options, headers: {
          ...options.headers, Authorization: `Token ${token}` } });
        if (resp.status === 401) await logout();
        return resp;
    };

    return <AuthContext.Provider value={{token, profileID, login, logout, authFetch}}>
        {children}
    </AuthContext.Provider>;
}

export function useAuth() {
    return useContext(AuthContext);
}