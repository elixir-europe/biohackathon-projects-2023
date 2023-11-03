/* Import Dependencies */
import axios from "axios";

/* Import Types */
import { VirtualReferenceCollection } from "app/types/VirtualReferenceCollection";


const GetVirtualReferenceCollection = async (virtualReferenceCollectionID: string) => {
    let virtualReferenceCollection: VirtualReferenceCollection = {} as VirtualReferenceCollection;

    if (virtualReferenceCollectionID) {
        let endPoint: string = `/vrc/${virtualReferenceCollectionID}`;

        try {
            const result = await axios({
                method: "get",
                url: endPoint,
                responseType: 'json'
            });

            /* Get result data from JSON */
            const data = result.data;

            /* Set Reference Collections */
            virtualReferenceCollection = data;
        } catch (error) {
            console.warn(error);
        }
    }

    return virtualReferenceCollection;
}

export default GetVirtualReferenceCollection;