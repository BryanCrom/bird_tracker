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
                    anchor={{ x: 0.5, y: 0.5 }}
                    coordinate={{latitude: -37.0118, longitude: 174.9076,}}
                    onPress={() => {router.push('/Stats')}}
                >
                    <View style={styles.icon}>
                        <CustomMarker />
                    </View>

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
    icon: {
        alignItems: 'center',
        justifyContent: 'center',
    }
});