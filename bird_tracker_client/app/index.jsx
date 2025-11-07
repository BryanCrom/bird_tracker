import React from 'react';
import MapView, {Marker} from 'react-native-maps';
import { StyleSheet, View } from 'react-native';
import { router } from 'expo-router';
import CustomMarker from "./CustomMarker";

const Home = () => {
    return (
        <View style={styles.container}>
            <MapView
                style={styles.map}
                initialRegion={{
                    latitude: -37.0118,
                    longitude: 174.9076,
                    latitudeDelta: 0.01,
                    longitudeDelta: 0.01,
                }}
            >
                <Marker
                    coordinate={{latitude: -37.0118, longitude: 174.9076,}}
                    onPress={() => {router.push('/Stats')}}
                >
                    <CustomMarker />
                </Marker>
            </MapView>
        </View>
    );
}

export default Home;

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    map: {
        width: '100%',
        height: '100%',
    },
});