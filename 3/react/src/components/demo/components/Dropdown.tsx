/* Import Dependencies */
import { useEffect, useState } from 'react';
import Select from 'react-select';

/* Import API */
import GetVirtualReferenceCollections from 'api/VirtualReferenceCollection/GetVirtualReferenceCollections';

/* Props Typing */
interface Props {
    selectedOption: string,
    SelectReferenceCollection: Function
}


const Dropdown = (props: Props) => {
    const { selectedOption, SelectReferenceCollection } = props;

    /* Base variables */
    const [options, setOptions] = useState<{ value: string, label: string }[]>([]);

    /* OnLoad: Fetch the Virtual Reference Collection options */
    useEffect(() => {
        GetVirtualReferenceCollections().then((virtualReferenceCollectionsList: string[]) => {
            if (virtualReferenceCollectionsList.length) {
                const options: { value: string, label: string }[] = [];

                virtualReferenceCollectionsList.forEach((virtualReferenceCollectionIndex) => {
                    options.push({
                        value: virtualReferenceCollectionIndex,
                        label: virtualReferenceCollectionIndex
                    });
                });

                setOptions(options);
            }
        }).catch(error => {
            console.warn(error);
        });
    }, []);

    return (
        <Select
            value={{
                value: selectedOption ? selectedOption : 'Select Taxon Virtual Reference Collection',
                label: selectedOption ? selectedOption : 'Select Virtual Reference Collection'
            }}
            options={options}
            className="text-white"
            isSearchable={false}
            styles={{
                control: provided => ({
                    ...provided, backgroundColor: '#4d59a2', border: '1px solid #4d59a2',
                    borderRadius: '999px', fontWeight: '500', fontSize: '0.875rem'
                }),
                menu: provided => ({
                    ...provided, zIndex: 100000, fontSize: '0.875rem', width: 'max-content',
                    position: 'absolute', right: '0', color: '#333333'
                }),
                dropdownIndicator: provided => ({ ...provided, color: 'white', fontSize: '0.875rem' }),
                singleValue: provided => ({
                    ...provided, color: 'white'
                })
            }}
            onChange={(option) => { if (option) { SelectReferenceCollection(option.value) } }}
        />
    );
}

export default Dropdown;