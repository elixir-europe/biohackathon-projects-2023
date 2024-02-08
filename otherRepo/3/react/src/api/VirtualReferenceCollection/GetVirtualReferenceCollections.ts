/* Import Dependencies */
import axios from 'axios'

/* Import Types */
import { VirtualReferenceCollection } from 'app/types/VirtualReferenceCollection';


const GetVirtualReferenceCollections = async () => {
    let virtualReferenceCollectionsList: string[] = [];

    let endPoint: string = '/vrc';

    try {
        const result = await axios({
            method: "get",
            url: endPoint,
            responseType: 'json'
        });

        /* Get result data from JSON */
        const data = result.data;

        /* Set Reference Collections */
        virtualReferenceCollectionsList = data;
    } catch (error) {
        console.warn(error);
    }

    return virtualReferenceCollectionsList;
}

export default GetVirtualReferenceCollections;