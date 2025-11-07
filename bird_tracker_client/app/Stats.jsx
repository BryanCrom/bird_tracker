import {StyleSheet, View, Text} from "react-native";
import { Link } from "expo-router";
import Graph from "./Graph";


const Stats = () => {
    return (
        <>
            <View style={styles.container}>
                <Text style={styles.title}>Statistics</Text>
                <Text style={styles.subtitle}>Location: The Auckland Botanical Gardens</Text>
                <Graph></Graph>
                <Link href="/" style={styles.card}>BACK</Link>
            </View>
        </>
    );
}

export default Stats;

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    title: {
        fontSize: 30,
        fontWeight: 'bold',
        alignSelf: 'center',
        marginTop: 20,
        margin: 10,
    },
    card: {
        backgroundColor: '#eee',
        padding: 10,
        borderRadius: 15,
        boxShadow: "4px 4px rgba(0,0,0,0.1)",
        alignSelf: 'center',
        margin: 20,
        fontSize: 18,
    },
    subtitle: {
        fontSize: 15,
        alignSelf: 'center',
        margin: 20,
    },
});