import speaker from "../assets/speaker.png";
import {StyleSheet, Image, View} from "react-native";
import React from "react";

const CustomMarker = () => {
    return(
        <View style={styles.card}>
            <Image
                source={speaker}
                style={styles.icon}
            />
        </View>
    );
}

export default CustomMarker;

const styles = StyleSheet.create({
    icon: {
        width: 20,
        height: 20,
    },
    card: {
        backgroundColor: '#eee',
        padding: 10,
        borderRadius: 5,
        boxShadow: "4px 4px rgba(0,0,0,0.1)",
    },
});